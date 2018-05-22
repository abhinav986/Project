import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { ToastService } from '../../typescripts/pro';

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.scss']
})
export class EditProfileComponent implements OnInit {
  optionsSelect = [];
  profileData: any = {};
  constructor(private profileService: ProfileService, private toast: ToastService) { }

  ngOnInit() {
    this.profileService.getProfile()
      .subscribe(profile_data => {
        this.profileData = profile_data;
        this.optionsSelect = this.profileData.languages;
      });
    this.getProfile();
  }

  getProfile() {
    this.profileService.getProfile()
      .subscribe(profile_data => {
        if (this.profileData.status == 1 || profile_data['status'] == 1) {
          this.profileData.firstName = profile_data['user'].firstName == 'undefined' ? '' : profile_data['user'].firstName;
          this.profileData.lastName = profile_data['user'].lastName == 'undefined' ? '' : profile_data['user'].lastName;
          this.profileData.headline = profile_data['user'].headline == 'undefined' ? '' : profile_data['user'].headline;
          this.profileData.biography = profile_data['user'].biography == 'undefined' ? '' : profile_data['user'].biography;
          this.profileData.websiteLink = profile_data['user'].websiteLink == 'undefined' ? '' : profile_data['user'].websiteLink;
          this.profileData.gplusLink = profile_data['user'].gplusLink == 'undefined' ? '' : profile_data['user'].gplusLink;
          this.profileData.twitterLink = profile_data['user'].twitterLink == 'undefined' ? '' : profile_data['user'].twitterLink;
          this.profileData.facebookLink = profile_data['user'].facebookLink == 'undefined' ? '' : profile_data['user'].facebookLink;
          this.profileData.youtubeLink = profile_data['user'].youtubeLink == 'undefined' ? '' : profile_data['user'].youtubeLink;
          this.profileData.language = "" + profile_data['user'].language;
        }
      });
  }

  saveProfile() {
    this.profileService.storeProfileData(this.profileData)
      .subscribe(data => {
        let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
        if (data['status'] == 1) {
          this.toast.success('', 'Your changes have been successfully saved.!', options);
          this.getProfile();
        } else {
          this.toast.error('', 'Oops! Someting went wrong.!', options);
          return false;
        }
      });
  }

}
