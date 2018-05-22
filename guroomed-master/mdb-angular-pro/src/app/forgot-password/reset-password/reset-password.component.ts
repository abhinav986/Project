import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';
import { Router } from '@angular/router';
import { ToastService } from '../../typescripts/pro';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.scss']
})
export class ResetPasswordComponent implements OnInit {
  confirmpassword: String;
  newpassword: String;
  message: String;
  reset = {};
  constructor(private nav: NavbarService, private route: Router, private toastrService: ToastService) { }

  ngOnInit() {
    this.nav.hide();
  }

  resetPassword() {

    if (this.newpassword == undefined) {
      return this.message = `Please enter new password`;
    }

    if (this.confirmpassword == undefined) {
      return this.message = `Please enter password to confirm`;
    }

    if (this.newpassword === this.confirmpassword) {
      this.reset = {
        newpass: this.newpassword
      }
      this.message = '';
      this.route.navigate(['']);
      let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
      this.toastrService.success('', 'Password successfully changed !', options);

    } else {
      this.message = `Password did'nt match`;
    }
  }

}
