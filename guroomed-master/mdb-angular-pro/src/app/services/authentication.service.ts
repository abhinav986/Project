import { Injectable } from '@angular/core';
import { tokenNotExpired, JwtHelper } from 'angular2-jwt';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class AuthenticationService {
  authToken;
  currentUser: string;
  loginUrl = '/api/frontend/login';
  signupUrl = '/api/frontend/signup/';
  forgotUrl = '/api/password_reset/';
  logoutUrl = 'api/frontend/logout';
  jwtHelper: JwtHelper = new JwtHelper();

  private headers = new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' });
  constructor(private http: HttpClient) { }

  // Function to login user
  login(user) {
    const body = `username=${user.username}&password=${user.password}`;
    return this.http.post(this.loginUrl, body, { headers: this.headers });
  }

  // Function to logout from current session
  logout() {
    this.authToken = null;
    this.currentUser = null;
    localStorage.removeItem('currentUser');
    localStorage.removeItem('user_id');
    localStorage.removeItem('token');
    return this.http.get(this.logoutUrl);
  }

  // Sign UP
  signUp(newUser) {
    const body = `first_name=${newUser.first_name}&last_name=${newUser.last_name}&email=${newUser.emailId}&password1=${newUser.password1}&password2=${newUser.password2}`;
    return this.http.post(this.signupUrl, body, { headers: this.headers });
  }

  // Function to store user data with token in local storage
  storeUserData(token, username) {
    var userId = this.jwtHelper.decodeToken(token);
    localStorage.setItem('token', token);
    localStorage.setItem('currentUser', JSON.stringify(username));
    localStorage.setItem('user_id', userId.user_id);
    this.authToken = token;
    this.currentUser = username;
  }

  // Forgot Password
  forgotPassword(userEmailId) {
    const body = `email=${userEmailId.email}`;
    return this.http.post(this.forgotUrl, body, { headers: this.headers });
  }

  loggedIn() {
    return tokenNotExpired();
  }

  getToken() {
    return localStorage.getItem('token');
  }

  getUserType() {
    if (tokenNotExpired()) {
      const token = this.jwtHelper.decodeToken(localStorage.getItem('token'));
      const userType = token.group_name;
      if (userType === 'Instructor') {
        return 'instructor';
      } else if (userType === 'Course Manager') {
        return 'manager';
      } else if (userType === 'Course Reviewer') {
        return 'reviewer';
      } else {
        return 'student';
      }
    }
  }
}
