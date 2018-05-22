import { Component, OnInit, ViewChild, Output, EventEmitter } from '@angular/core';
import { AuthenticationService } from 'app/services/authentication.service';
import { ModalDirective } from 'app/typescripts/free';
import { ShoppingcartService } from '../services/shopcart/shoppingcart.service';
import { ToastService } from '../typescripts/pro';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loading: boolean;
  @ViewChild('autoShownModal')
  loginMessage = '';
  credentials: any = {};
  localStorageCartItem;

  @Output() onLoggedIn = new EventEmitter();

  constructor(private authService: AuthenticationService,
    public autoShownModal: ModalDirective,
    private shoppingCartService: ShoppingcartService,
    private toastrService: ToastService,
    private router: Router
  ) { }

  ngOnInit() {
  }

  onLoginSubmit() {
    const user = {
      username: this.credentials.username,
      password: this.credentials.password
    }
    this.loading = true;
    this.authService.login(user).subscribe(data => {
      this.loading = false;
      if (data['status'] === 0) {
        this.loginMessage = data['error'];
      } else {
        this.loginMessage = '';

        this.authService.storeUserData(data['access_token'], user.username);
        this.autoShownModal.hide();

        const options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
        this.toastrService.success('', 'Successfully signed in as "' + user.username + '"', options);

        if (this.authService.getUserType() === 'manager') {
          this.router.navigate(['/course-management', 'dashboard', 'all']);
        } else if (this.authService.getUserType() === 'reviewer') {
          this.router.navigate(['/course-reviewer', 'dashboard', 'all']);
        }

        this.onLoggedIn.emit('true');

        if (localStorage.getItem('cart_key') != null) {
          this.localStorageCartItem = JSON.parse(localStorage.getItem('cart_key'));
          this.shoppingCartService.addItem(this.localStorageCartItem);
          localStorage.removeItem('cart_key');
          this.shoppingCartService.getCartItem(localStorage.getItem('user_id')).subscribe(data => {
            this.shoppingCartService.cartCounter(data['count']);
          });
        }
        this.shoppingCartService.getCartItem(localStorage.getItem('user_id')).subscribe(data => {
          this.shoppingCartService.cartCounter(data['count']);
        });

        if (this.router.url === '/cart') {
          this.router.navigate(['cart', 'items']);
        }
      }
    });
  }

}
