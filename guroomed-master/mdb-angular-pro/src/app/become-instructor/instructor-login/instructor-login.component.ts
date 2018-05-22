import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';
import { ActivatedRoute } from '@angular/router';
import { InstructorServiceService } from '../instructor-service/instructor-service.service';
import { AuthenticationService } from '../../services/authentication.service';

@Component({
  selector: 'app-instructor-login',
  templateUrl: './instructor-login.component.html',
  styleUrls: ['./instructor-login.component.scss']
})
export class InstructorLoginComponent implements OnInit {
  errorMsg: string;
  successMsg: string;
  instructorCredentials: any = {}
  constructor(private nav: NavbarService, private route: ActivatedRoute, private instructorService: InstructorServiceService, private authenticationService: AuthenticationService) { }

  ngOnInit() {
    this.nav.show();
    this.getUrlData();
  }

  getUrlData() {
    var uidb64, token;
    this.route.queryParams.subscribe(param => {
      uidb64 = param.uidb64;
      token = param.token;

    });
    if (uidb64 != undefined && token != undefined) {
      this.instructorService.emailVerification(uidb64, token).subscribe(res => {
        console.log(res);
        if (res['status'] === 1) {
          // Refreshing token after email verification
          if (this.authenticationService.loggedIn()) {
            this.instructorService.getToken().subscribe((token) => {
              console.log(token);
              if (token['status'] === 1) {
                this.authenticationService.storeUserData(token['access_token'], (localStorage.getItem('currentUser')));
              }
            });
          }
          this.successMsg = res['msg'];
        } else {
          this.errorMsg = 'Link Expired';
        }
      });
    }
  }
}
