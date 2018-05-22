import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';
import { SignupService } from './signup.service';
import { ToastService } from '../../typescripts/pro';
import { AuthenticationService } from '../../services/authentication.service';
import { ProfileService } from '../../profile/profile.service';

@Component({
  selector: 'app-instructor-sign-up',
  templateUrl: './instructor-sign-up.component.html',
  styleUrls: ['./instructor-sign-up.component.scss']
})
export class InstructorSignUpComponent implements OnInit {
  alreadyLoggedIn: boolean;
  loading: boolean = false;
  success: boolean = false;
  response: any;
  instructorSignUpData: any = {};
  isInstructor: boolean;
  constructor(private nav: NavbarService, private signUpService: SignupService, private toastService: ToastService,
    private authService: AuthenticationService, private profileService: ProfileService) { }

  ngOnInit() {
    this.nav.show();
    this.instructorSignUpData.get_information = false;
    this.instructorSignUpData.isInstructor = true;

    if (this.authService.loggedIn()) {
      this.alreadyLoggedIn = true;
      this.profileService.getProfile().subscribe(res => {
        this.instructorSignUpData.firstName = res['user'].firstName;
        this.instructorSignUpData.lastName = res['user'].lastName;
        this.instructorSignUpData.emailId = res['user'].email;
      });
    } else {
      this.alreadyLoggedIn = false;
    }
  }

  instrunctorSignUp() {
    this.loading = true;
    this.signUpService.instructorSignUp(this.instructorSignUpData).subscribe(res => {
      let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
      if (res['status'] == 0) {
        this.loading = false;
        this.toastService.error('', res['error'], options);
      } else if (res['status'] == 1) {
        this.loading = false;
        this.success = true;
        this.response = res['msg'];
      }
    });
  }

}
