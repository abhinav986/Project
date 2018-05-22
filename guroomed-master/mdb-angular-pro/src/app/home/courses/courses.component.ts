import { Component, OnInit, Input } from '@angular/core';
import { ShoppingcartService } from '../../services/shopcart/shoppingcart.service';
import { AuthenticationService } from '../../services/authentication.service';
import { Router } from '@angular/router';
import { ToastService } from '../../typescripts/pro';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.scss']
})
export class CoursesComponent implements OnInit {
  goToCartButton: boolean;
  options;
  preview_url: string;
  public _data: any;
  private storage: Storage;

  @Input()

  set data(data: any) {
    this._data = data;
    if (window.location.port == '4200') {
      this.preview_url = 'http://127.0.0.1:8000' + this._data.preview_image_url;
    } else {
      this.preview_url = 'http://www.guroomed.com' + this._data.preview_image_url;
    }
  }

  get data(): any {
    return this._data;
  }

  constructor(private shoppingCartService: ShoppingcartService,
    private authenticationService: AuthenticationService,
    private router: Router,
    private toastrService: ToastService) { }

  ngOnInit() {
    this.addedToCart(this._data.course_id);
    this.options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
  }

  addToCart(courseData) {

    if (this.authenticationService.loggedIn()) {
      this.shoppingCartService.addItem(courseData)
        .subscribe(data => {
          if (data.status == 1) {
            this.goToCartButton = true;
            this.toastrService.success('', 'Course added to cart !', this.options);
          } else {
            this.goToCartButton = false;
          }
          this.shoppingCartService.cartCounter(data.count);
        });
    } else {
      this.shoppingCartService.addItem(courseData);
      this.toastrService.success('', 'Course added to cart !', this.options);
      this.addedToCart(courseData.course_id);
      var countItem = JSON.parse(localStorage.getItem('cart_key'));
      this.shoppingCartService.cartCounter(countItem.items.length);
    }
  }

  addedToCart(id) {
    if (localStorage.getItem('cart_key') != null) {
      this.storage = JSON.parse(localStorage.getItem('cart_key'));
      this.storage.items.find(element => {
        if (element.courseId == id) {
          return this.goToCartButton = true;
        } else {
          return this.goToCartButton = false;
        }
      });
    }

    if (this.authenticationService.loggedIn()) {
      this.shoppingCartService.getCartItem(localStorage.getItem('user_id'))
        .subscribe(data => {
          data['items'].find(element => {
            if (element.courseId == id) {
              return this.goToCartButton = true;
            } else {
              return this.goToCartButton = false;
            }
          });
        });
    }
  }

  goToCart() {
    this.router.navigate(['cart']);
  }

}
