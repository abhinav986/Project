import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { InstructorServiceService } from '../../instructor-service/instructor-service.service';
import { ToastService } from '../../../typescripts/pro';

@Component({
  selector: 'app-course-basics',
  templateUrl: './course-basics.component.html',
  styleUrls: ['./course-basics.component.scss']
})
export class CourseBasicsComponent implements OnInit {
  processing: boolean;
  videoFileToUpload: any;
  course_id: number;
  videoUrl: any;
  error: string;
  fileToUpload: any;
  loading: boolean = false;
  imageUrl: string;
  languageList = [];
  levelList = [];
  categoryList = [];
  basicCourse: any = {};
  percentComplete: number = 0;
  constructor(private route: ActivatedRoute, private toastService: ToastService, private instructorService: InstructorServiceService) { }

  ngOnInit() {
    if (window.location.port == '4200') {
      this.imageUrl = 'http://127.0.0.1:8000/media/image-placeholder.png';
    } else {
      this.imageUrl = 'http://www.guroomed.com/media/image-placeholder.png';
    }
    this.course_id = this.route.snapshot.parent.params.id;
    this.instructorService.getList(this.course_id).subscribe(data => {
      this.languageList = data['languages'];
      this.levelList = data['levels'];
      this.categoryList = data['sub_cats'];
    });
    this.getList(this.course_id);
  }

  getList(course_id) {
    this.instructorService.getList(course_id).subscribe(data => {
      this.basicCourse.course_title = data['draft'].course_title;
      this.basicCourse.course_subtitle = data['draft'].course_subtitle;
      this.basicCourse.course_price = data['draft'].course_price;
      if (data['draft'].language != null) {
        this.basicCourse.language = [data['draft'].language.value];
      }
      this.basicCourse.level = [data['draft'].level.value];
      if (data['draft'].subcategory != null) {
      this.basicCourse.category = [data['draft'].subcategory.value];
      }
    });
  }

  imageUpload(file: FileList): void {

    this.fileToUpload = file.item(0);

    if (this.fileToUpload != null) {
      var fileType = this.fileToUpload.type.split('/').shift();
      //For image file upload
      if (fileType == 'image') {
        var fileExtension = this.fileToUpload.name.split('.').pop();
        if (fileExtension == 'jpeg' || fileExtension == 'jpg' || fileExtension == 'png') {
          if (this.fileToUpload.size < 512000) {
            this.error = '';
            var reader = new FileReader();
            reader.onload = (e: any) => {
              var image = new Image();
              image.onload = () => {
                if (image.width >= 750 && image.height >= 422) {
                  this.loading = true;
                  // this.profileService.uploadImage(this.fileToUpload).subscribe(data => {
                  //   this.imageUrl = 'http://127.0.0.1:8000' + data.link;
                  //   this.error = '';
                  //   this.loading = false;
                  // });
                  this.imageUrl = e.target.result;
                  this.loading = false;
                } else {
                  this.error = 'The image you want upload is too small. Minimum image size is 750px x 422px. Please upload a larger image.';
                  reader = null;
                }
              }
              image.src = e.target.result;
            }
            reader.onprogress = (event: any) => {
              if (event.lengthComputable) {
                this.percentComplete = (event.loaded / event.total) * 100;
              }
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

  videoUpload(videoFile: FileList) {
    this.videoFileToUpload = videoFile.item(0);
    if (this.videoFileToUpload) {
      var videoFileReader = new FileReader();
      videoFileReader.readAsDataURL(this.videoFileToUpload)
    }
  }

  onSubmitBasicCourse(event) {
    event.preventDefault();
    let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
    if (this.basicCourse.course_title == undefined || this.basicCourse.course_subtitle == undefined || this.basicCourse.language == undefined || this.basicCourse.level == undefined || this.basicCourse.category == undefined || this.basicCourse.course_price == undefined) {
      this.toastService.error('', 'Please fill all the mandatory field', options);
    } else {
      this.processing = true;
      this.instructorService.saveCourseBasics(this.course_id, this.basicCourse, this.fileToUpload, this.videoFileToUpload).subscribe(res => {
        this.processing = false;
        if (res['status'] == 1) {
          this.toastService.success('', res['msg'], options);
        } else {
          this.toastService.error('', 'Something went wrong..! ', options);
        }
      });
    }
  }

}
