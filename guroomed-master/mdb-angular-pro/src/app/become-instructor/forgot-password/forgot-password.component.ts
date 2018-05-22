import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})
export class ForgotPasswordComponent implements OnInit {
  resetEmailId: any = {};
  constructor(private nav: NavbarService) { }

  ngOnInit() {
    this.nav.show();
  }

  onSubmitForgotPassword(){
    console.log(this.resetEmailId);
  }

}
