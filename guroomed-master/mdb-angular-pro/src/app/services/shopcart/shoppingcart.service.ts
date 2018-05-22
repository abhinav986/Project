import { Injectable } from '@angular/core';
import { StorageService } from 'app/services/localstore/storage.service';
import { ShoppingCart } from 'app/models/shopping-cart.model';
import { CartItem } from 'app/models/cart-item.model';
import { AuthenticationService } from 'app/services/authentication.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';
import { Subject } from 'rxjs/Subject';

@Injectable()
export class ShoppingcartService {
  private subject = new Subject<any>();

  private storage: Storage;
  userId: string;
  addedCart;

  cartUrl: string = '/api/usercart/add';
  private headers = new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' });

  constructor(
    private http: HttpClient,
    private storageService: StorageService,
    private authenticationService: AuthenticationService,
  ) {
    this.storage = this.storageService.get();
  }

  addItem(courseData) {
    this.userId = localStorage.getItem('user_id');
    if (courseData.items) {
      courseData.items.forEach(element => {
        var body = `user_id=${this.userId}&course_ids[]=${element.courseId}`;
        this.addedCart = this.http.post(this.cartUrl, body, { headers: this.headers }).subscribe(res => res);
      });
      return this.addedCart;
    }

    // if user is loggedin then storing cart items in DB. Otherwise in localstorage.
    if (this.authenticationService.loggedIn()) {
      if (courseData.course_id) {
        var body = `user_id=${this.userId}&course_ids[]=${courseData.course_id}`;
      } else {
        var body = `user_id=${this.userId}&course_ids[]=${courseData.id}`;
      }
      return this.http.post(this.cartUrl, body, { headers: this.headers });
    } else {
      const cart = this.retrieve();
      if (courseData.course_id) {
        var item = cart.items.find((course) => course.courseId === courseData.course_id);
      } else {
        var item = cart.items.find((course) => course.courseId === courseData.id);
      }

      if (item === undefined) {
        item = new CartItem();
        if (courseData.course_id) {
          item.courseId = courseData.course_id;
        } else {
          item.courseId = courseData.id;
        }
        cart.items.push(item);
      }
      this.save(cart);
    }
  }

  getCartItem(user_id) {
    return this.http.get(`api/usercart/get/${user_id}`);
  }

  removeItem(data) {
    if (this.authenticationService.loggedIn()) {
      this.userId = localStorage.getItem('user_id');
      let body = `course_id=${data.id}`;
      return this.http.post(`api/usercart/delete/${this.userId}`, body, { headers: this.headers });
    } else {
      const cart = this.retrieve();
      let item = cart.items.find((course) => course.courseId == data.id);
      let index = cart.items.indexOf(item);
      cart.items.splice(index, 1);
      this.save(cart);
    }
  }

  private save(cart: ShoppingCart): void {
    this.storage.setItem('cart_key', JSON.stringify(cart));
  }

  public retrieve(): ShoppingCart {
    const cart = new ShoppingCart();
    const storedCart = this.storage.getItem('cart_key');

    if (storedCart) {
      cart.updateFrom(JSON.parse(storedCart));
    }
    return cart;
  }

  cartCounter(counter: string) {
    this.subject.next(counter);
  }

  clearMessage() {
    this.subject.next();
  }

  getMessage(): Observable<any> {
    return this.subject.asObservable();
  }

}
