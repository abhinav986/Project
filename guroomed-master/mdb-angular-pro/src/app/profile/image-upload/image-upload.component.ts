import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';

@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.component.html',
  styleUrls: ['./image-upload.component.scss']
})
export class ImageUploadComponent implements OnInit {
  error: string = '';
  test: boolean = false;
  newimage: any;
  loading: boolean;
  imageUrl: string;
  photo_link;
  fileToUpload: File = null;
  constructor(private profileService: ProfileService) { }

  ngOnInit() {
    this.profileService.getProfile().subscribe(profileData => {
      if (profileData['user'].photoLink == '' || profileData['user'].photoLink == null || profileData['user'].photoLink == undefined) {
        this.imageUrl = 'https://www.udemy.com/staticx/udemy/images/course/750x422/placeholder.png';
      } else {
        if (window.location.port == '4200') {
          this.imageUrl = 'http://127.0.0.1:8000/media/' + profileData['user'].photoLink;
        } else {
          this.imageUrl = 'http://www.guroomed.com/media/' + profileData['user'].photoLink;
        }
      }
    });
  }

  uploadImage(file: FileList) {
    this.fileToUpload = file.item(0);
    if (this.fileToUpload != null) {
      var fileExtension = this.fileToUpload.name.split('.').pop();
      if (fileExtension == 'jpeg' || fileExtension == 'jpg' || fileExtension == 'png') {
        if (this.fileToUpload.size < 512000) {
          this.error = '';
          var reader = new FileReader();
          reader.onload = (e: any) => {
            var image = new Image();
            image.onload = () => {
              if (image.width >= 200 && image.height >= 200) {
                this.loading = true;
                this.profileService.uploadImage(this.fileToUpload).subscribe(data => {
                  this.imageUrl = 'http://127.0.0.1:8000' + data['link'];
                  this.error = '';
                  this.loading = false;
                });
              } else {
                this.error = 'The image you want upload is too small. Minimum image size is 200x200px. Please upload a larger image.';
                reader = null;
              }
            }
            image.src = e.target.result;
          }
          reader.readAsDataURL(this.fileToUpload);
        } else {
          this.error = 'File size should not be more that 0.5MB'
        }
      } else {
        this.error = 'File type not supported.'
      }
    }
  }

}
