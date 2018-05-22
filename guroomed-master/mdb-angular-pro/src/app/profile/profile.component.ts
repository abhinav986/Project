import { Component, OnInit } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { ProfileService } from './profile.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  nameImagePlaceholder: string = '';
  profileImage: string;
  currentUser: string;
  constructor(private nav: NavbarService, private profileService: ProfileService) { }

  ngOnInit() {
    this.nav.show();
    this.currentUser = localStorage.getItem('currentUser').replace(/"/g, '');
    this.profileService.getProfile().subscribe(profileData => {
      if (profileData['user'].photoLink == undefined || profileData['user'].photoLink == null || profileData['user'].photoLink == '') {
        var firstName = profileData['user'].firstName.charAt(0);
        var lastName = profileData['user'].lastName.charAt(0);
        this.nameImagePlaceholder = firstName+lastName;
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

}