import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { MycoursesService } from '../mycourses.service';

@Component({
  selector: 'app-learning',
  templateUrl: './learning.component.html',
  styleUrls: ['./learning.component.scss']
})
export class LearningComponent implements OnInit {
  image_url: boolean;
  video_id: any;
  myCourseData: any;
  isCourseData: boolean = true;

  constructor(private router: Router, private nav: NavbarService, private myCourse: MycoursesService) { }

  ngOnInit() {
    this.nav.show();
    this.myCourse.getMyCourses(localStorage.getItem('user_id')).subscribe(data => {
        this.myCourseData = data['courses'];
        if (this.myCourseData.length == 0) {
          this.isCourseData = false;
        }
      });

    if (window.location.port == '4200') {
      this.image_url = true;
    } else {
      this.image_url = false;
    }
  }

  onLecturesClick(course_id) {
    this.myCourse.getMyCourseVideos(course_id)
      .subscribe(data => {
        if (data['curriculum'].length > 0) {
          this.video_id = data['curriculum'][0].curriculumLect[0].video_url;
          if (this.video_id) {
            this.router.navigate(['lectures', { id: course_id, video_id: this.video_id }]);
          }
        }
      });
  }

  courseDetails(course_id){
    this.router.navigate(['coursedetails', course_id]);
  }

  goToHome() {
    this.router.navigate(['']);
  }

}
