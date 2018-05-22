import { Component, OnInit } from '@angular/core';
import { MycoursesService } from '../mycourses.service';
import { ActivatedRoute, Router } from '@angular/router';
import { InstructorServiceService } from '../../become-instructor/instructor-service/instructor-service.service';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.scss']
})
export class SideNavComponent implements OnInit {

  currentUrl: string;
  sideNavOpened: boolean;
  url: any;
  itemsList: any;
  course_id: any;

  constructor(private myCourse: MycoursesService, private router: Router, private route: ActivatedRoute, private instructorService: InstructorServiceService) { }

  ngOnInit() {

    this.route.params.subscribe(params => {
      this.course_id = params.id;
    });

    this.currentUrl = this.route.snapshot.routeConfig.path.split('/')[2];

    if (this.currentUrl == 'draft-content') {
      this.getDraftLecture(this.course_id);
    } else {
      this.getUserLecture(this.course_id);
    }

  }

  getDraftLecture(course_id) {
    this.instructorService.getCurriculum(course_id).subscribe(data => {
      if (data['status'] == 1) {
        this.itemsList = data['curriculum'].reverse();
      }
    });
  }

  getUserLecture(course_id) {
    this.myCourse.getMyCourseVideos(course_id)
      .subscribe(data => {
        this.itemsList = data['curriculum'];
      });
  }

  getUrl(a) {
    this.url = a.preview_url;
    // this.closeNav();
    if (this.currentUrl == 'draft-content') {
      if (this.url) {
        this.router.navigate(['instructor', 'course', 'draft-content', 'lecture', { id: this.course_id, video_id: this.url }]);
      } else{
        this.router.navigate(['instructor', 'course', 'draft-content', 'quiz', { id: this.course_id, quiz_id: a.id}])
      }
    } else {
        this.router.navigate(['/lectures', { id: this.course_id, video_id: this.url }]);
    }
  }

}
