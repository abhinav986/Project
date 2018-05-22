import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../../profile/profile.service';
import { AuthenticationService } from '../../services/authentication.service';
import { Router } from '@angular/router';
import { ToastService } from '../../typescripts/pro';

@Component({
  selector: 'app-management-navbar',
  templateUrl: './management-navbar.component.html',
  styleUrls: ['./management-navbar.component.scss']
})
export class ManagementNavbarComponent implements OnInit {

  userType: string;
  profileImage: string;
  nameImagePlaceholder: any;
  constructor(private profileService: ProfileService, private authService: AuthenticationService, private router: Router, private toastService: ToastService) { }

  ngOnInit() {
    this.userType = this.authService.getUserType();
    this.getProfile();
  }

  getProfile() {
    this.profileService.getProfile().subscribe(profileData => {
      if (profileData['user'].photoLink == undefined || profileData['user'].photoLink == null || profileData['user'].photoLink == '') {
        var firstName = profileData['user'].firstName.charAt(0);
        var lastName = profileData['user'].lastName.charAt(0);
        this.nameImagePlaceholder = firstName + lastName;
      } else {
        this.nameImagePlaceholder = '';
        if (window.location.port == '4200') {
          this.profileImage = 'http://127.0.0.1:8000/media/' + profileData['user'].photoLink;
        } else {
          this.profileImage = 'http://www.guroomed.com/media/' + profileData['user'].photoLink;
        }
      }
    });
  }

  logout() {
    this.authService.logout().subscribe(data => {
      if (data['status'] == 1) {
        this.router.navigate(['/']);
        let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
        this.toastService.success('', 'You are logged out successfully !', options);
      }
    });
  }


}
