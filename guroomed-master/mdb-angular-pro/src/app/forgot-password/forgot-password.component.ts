import { Component, OnInit, ViewChild } from '@angular/core';
import { AuthenticationService } from 'app/services/authentication.service';
import { ModalDirective } from 'app/typescripts/free';
import { Router } from '@angular/router';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})
export class ForgotPasswordComponent implements OnInit {

  @ViewChild('autoShownModal')
  user_emailId: string;
  message: string;
  resetEmail: any = {};
  constructor(
    private authService: AuthenticationService,
    public autoShownModal: ModalDirective,
    public route: Router
  ) { }

  ngOnInit() {
  }

  onSubmitForgotPassword() {
    const userEmailId = {
      email: this.resetEmail.user_emailId
    }

    this.authService.forgotPassword(userEmailId)
      .subscribe(res => {
        if (res['status'] === 1) {
          this.autoShownModal.hide();
          this.route.navigate(['/forgotSuccessMsg']);
        }
      });
  }
}
