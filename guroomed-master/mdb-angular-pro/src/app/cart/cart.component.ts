import { Component, OnInit } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { Router } from '@angular/router';
import { StorageService } from 'app/services/localstore/storage.service';
import { CourseDetailService } from 'app/services/coursedetail/course-detail.service';
import { ShoppingcartService } from 'app/services/shopcart/shoppingcart.service';
import { LoaderService } from 'app/shared/loader/loader.service';
import { AuthenticationService } from '../services/authentication.service';
import { ToastService } from '../typescripts/pro';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {
  image_url: boolean;
  hideEmptyCart: boolean;
  errorMessage: any;
  cartData: any;
  cartData1: any = [];
  discountTotal: any = 0;
  totalPrice: any = 0;
  options;

  private storage: Storage;

  constructor(
    private nav: NavbarService,
    private loader: LoaderService,
    private route: Router,
    private storageService: StorageService,
    private courseDetails: CourseDetailService,
    private shoppingCartService: ShoppingcartService,
    private authenticationService: AuthenticationService,
    private toastrService: ToastService

  ) {
    this.storage = this.storageService.get();
  }

  ngOnInit() {
    this.nav.show();
    this.loader.show();
    this.storedCartData();
    this.loader.hide();
    this.options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };

    if(window.location.port == '4200') {
      this.image_url = true;
    } else {
      this.image_url = false;
    }
  }

  storedCartData() {
    if (this.storage.getItem('cart_key')) {
      this.storage = JSON.parse(this.storage.cart_key);
      this.cartData = this.storage.items.forEach(element => {
        this.courseDetails.get(element.courseId)
          .subscribe(courseDetailsData => {
            this.cartData = courseDetailsData;
            this.cartData1.push(this.cartData);
            this.discountTotal = this.discountTotal + this.cartData.discount;
            this.totalPrice = this.totalPrice + this.cartData.price;
            this.hideEmptyCart = true;

          },
            error => this.errorMessage = <any>error
          );
      });
    }
    if (this.authenticationService.loggedIn()) {
      this.shoppingCartService.getCartItem(localStorage.getItem('user_id'))
        .subscribe(data => {
          this.cartData = data['items'].forEach(element => {
            this.courseDetails.get(element.courseId)
              .subscribe(courseDetailsData => {
                this.cartData = courseDetailsData;
                this.cartData1.push(this.cartData);
                this.discountTotal = this.discountTotal + this.cartData.discount;
                this.totalPrice = this.totalPrice + this.cartData.price;
                this.hideEmptyCart = true;
              },
                error => this.errorMessage = <any>error
              );
          });
        })
    }
  }

  removeItem(cart) {
    let index = this.cartData1.indexOf(cart);
    this.cartData1.splice(index, 1);
    if (this.authenticationService.loggedIn()) {
      this.shoppingCartService.removeItem(cart)
        .subscribe(data => {
          this.shoppingCartService.cartCounter(data['count']);
        });
        
    } else {
      this.shoppingCartService.removeItem(cart);
      var countItem = JSON.parse(localStorage.getItem('cart_key'));
      this.shoppingCartService.cartCounter(countItem.items.length);
    }
    this.toastrService.success('Removed from cart.. !', cart.title, this.options);
    this.discountTotal = this.discountTotal - cart.discount;
    this.totalPrice = this.totalPrice - cart.price;
  }

  getCourseDetail(courseId: number) {
    this.route.navigate(['coursedetails', courseId]);
  }

  keepShopping() {
    this.route.navigate(['']);
  }

  checkOut() {
    if (this.authenticationService.loggedIn()) {
      this.route.navigate(['checkout']);
    } else {
      this.toastrService.info('', 'Please login to continue.... !', this.options);
    }
  }
}
