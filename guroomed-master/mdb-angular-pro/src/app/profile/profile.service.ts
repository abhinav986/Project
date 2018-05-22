import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class ProfileService {
  getprofileUrl = '/api/users/profile/';
  storeProfileUrl = '/api/users/profile/store';
  chnagePasswordUrl = 'api/password_change/';
  uploadImageUrl = '/api/users/profile/store/picture'
  private headers = new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' });
  constructor(private http: HttpClient) { }

  getProfile() {
    return this.http.get(this.getprofileUrl);
  }

  storeProfileData(profileData) {
    let body = `first_name=${profileData.firstName}&last_name=${profileData.lastName}&headline=${profileData.headline}&biography=${profileData.biography}&language=${profileData.language}&website_link=${profileData.websiteLink}&gplus_link=${profileData.gplusLink}&twitter_link=${profileData.twitterLink}&facebook_link=${profileData.facebookLink}&linkedin_link=${profileData.linkedinLink}&youtube_link=${profileData.youtubeLink}`;
    return this.http.post(this.storeProfileUrl, body, { headers: this.headers });
  }

  changePassword(changeUserPassword) {
    let body = `password1=${changeUserPassword.currentPassword}&password2=${changeUserPassword.password2}`;
    return this.http.post(this.chnagePasswordUrl, body, { headers: this.headers });
  }

  uploadImage(photo_link: File) {
    var formData: FormData = new FormData();
    formData.append('photo_link', photo_link, photo_link.name);
    return this.http.post(this.uploadImageUrl, formData);
  }
}
