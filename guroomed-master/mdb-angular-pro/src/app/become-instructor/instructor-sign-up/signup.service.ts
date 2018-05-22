import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthenticationService } from '../../services/authentication.service';

@Injectable()
export class SignupService {

  signUpUrl = 'api/courses/instructor/signup';
  private headers = new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' });
  constructor(private http: HttpClient, private authService: AuthenticationService) { }


  instructorSignUp(instructorSignUpData) {
    var body;
    if (this.authService.loggedIn()) {
      body = `first_name=${instructorSignUpData.firstName}&last_name=${instructorSignUpData.lastName}&email=${instructorSignUpData.emailId}&password=${instructorSignUpData.new_password}`;
    } else {
      body = `first_name=${instructorSignUpData.firstName}&last_name=${instructorSignUpData.lastName}&email=${instructorSignUpData.emailId}&password1=${instructorSignUpData.new_password}&password2=${instructorSignUpData.confirmPassword}`;
    }
    return this.http.post(this.signUpUrl, body, { headers: this.headers })
      .map(res => res);
  }

}
