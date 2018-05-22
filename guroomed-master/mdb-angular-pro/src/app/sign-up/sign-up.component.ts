import { Component, OnInit, ViewChild } from '@angular/core';
import { ModalDirective } from 'app/typescripts/free';
import { AuthenticationService } from 'app/services/authentication.service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent implements OnInit {
  loading: boolean;
  @ViewChild('autoShownModal')
  firstName: string;
  lastName: string;
  emailId: string;
  new_password: string;
  confirmPassword: string;
  signupError: string;
  signUpData: any = {};
  constructor(public autoShownModal: ModalDirective, private authenticationService: AuthenticationService) {
  }

  ngOnInit() {
  }

  onSubmitSignUP() {
    const newUser = {
      first_name: this.signUpData.firstName,
      last_name: this.signUpData.lastName,
      emailId: this.signUpData.emailId,
      password1: this.signUpData.new_password,
      password2: this.signUpData.confirmPassword
    }

    if (newUser.password1 !== newUser.password2) {
      this.signupError = 'Password not matched';
      return false;
    }

    this.loading = true;
    this.authenticationService.signUp(newUser).subscribe(data => {
      this.loading = false;
      if (data['status'] === 0) {
        this.signupError = data['error'];
      } else if (data['status'] === 1) {
        const user = {
          username: this.signUpData.emailId,
          password: this.signUpData.new_password,
        }
        this.authenticationService.login(user).subscribe(data => {
          this.authenticationService.storeUserData(data['access_token'], user.username);
        });
        this.autoShownModal.hide();
      }
    });
  }
}
