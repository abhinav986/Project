import { Component, OnInit, OnDestroy } from '@angular/core';
import { AuthenticationService } from 'app/services/authentication.service';
import { Router } from '@angular/router';
import { NavbarService } from '../navbarService/navbar.service';
import { ToastService } from '../../typescripts/pro';

import { Subscription } from 'rxjs/Subscription';
import { ShoppingcartService } from '../../services/shopcart/shoppingcart.service';
import { ProfileService } from '../../profile/profile.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit, OnDestroy {

  nameImagePlaceholder: string = '';
  profileImage: any;
  counter: any;
  subscription: Subscription;

  currentUser: string;
  count: number;
  constructor(
    private authService: AuthenticationService,
    private router: Router,
    public nav: NavbarService,
    private toastrService: ToastService,
    private shoppingService: ShoppingcartService,
    private profileService: ProfileService
  ) { }

  ngOnInit() {
    if (this.shoppingService.retrieve().items.length > 0) {
      this.counter = this.shoppingService.retrieve().items.length;
    }
    this.subscription = this.shoppingService.getMessage().subscribe(counter => {
      this.counter = counter;
    });
    this.getProfile();
  }

  getProfile() {
    if (this.authService.loggedIn()) {
      this.profileService.getProfile().subscribe(profileData => {
        if (profileData['user'].photoLink === undefined || profileData['user'].photoLink === null || profileData['user'].photoLink === '') {
          let firstName = profileData['user'].firstName.charAt(0);
          let lastName = profileData['user'].lastName.charAt(0);
          this.nameImagePlaceholder = firstName + lastName;
        } else {
          this.nameImagePlaceholder = '';
          if (window.location.port === '4200') {
            this.profileImage = 'http://127.0.0.1:8000/media/' + profileData['user'].photoLink;
          } else {
            this.profileImage = 'http://www.guroomed.com/media/' + profileData['user'].photoLink;
          }
        }
      });
    }
  }

  onLogoutClick() {
    this.authService.logout().subscribe(data => {
      if (data['status'] === 1) {
        this.router.navigate(['/']);
        const options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
        this.toastrService.success('', 'You are logged out successfully !', options);
        this.shoppingService.cartCounter('');
      }
    });
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}