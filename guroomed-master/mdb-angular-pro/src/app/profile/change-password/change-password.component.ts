import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { AuthenticationService } from '../../services/authentication.service';
import { Router } from '@angular/router';
import {ToastService} from '../../typescripts/pro/alerts'

@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.scss']
})
export class ChangePasswordComponent implements OnInit {
  retypePassword: String;
  newPassword: String;
  currentPassword: String;
  changeUserPassword = {};
  error: String;
  constructor(private profileService: ProfileService, private router: Router, private authService: AuthenticationService,private toast: ToastService ) { }

  ngOnInit() {

  }

  changePassword() {

    if (this.currentPassword == undefined){
      this.error = "Enter Current Password";
      return false;
    } else if (this.newPassword == undefined){
      this.error = "Enter New Password";
      return false;
    } else if (this.retypePassword == undefined ){
      this.error = "Re-type New Password";
      return false;
    }

    if(this.newPassword != this.retypePassword ) {
      this.error = "Password didn't match"
      return false;
    }

    this.changeUserPassword = {
      currentPassword: this.currentPassword,
      password1: this.newPassword,
      password2: this.retypePassword
    }


    this.profileService.changePassword(this.changeUserPassword)
      .subscribe(data => {
        if (data['status'] == 0) {
          this.error = data['error'];
          return false;
        } else if (data['status'] == 1) {
          this.authService.logout();
            let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-bottom-right' };
            this.toast.success('Please login with new password.','Password Changed Successfully!', options);
          this.router.navigate(['/']);
        }
      });
  }

}
