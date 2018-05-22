import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../shared/navbarService/navbar.service';
import { ManagementService } from '../course-management/course-manager/management.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-course-overview',
  templateUrl: './course-overview.component.html',
  styleUrls: ['./course-overview.component.scss']
})
export class CourseOverviewComponent implements OnInit {

  courseTitle: any;
  draftCourse: any;
  course_id: any;
  constructor(private nav: NavbarService, private managementService: ManagementService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.nav.show();
    this.course_id = this.route.snapshot.params.id;
    this.getCourse(this.course_id);
  }

  getCourse(course_id){
    this.managementService.getCourseStatus(course_id).subscribe( res => {
      this.draftCourse = res['draft_course'];
      this.courseTitle = this.draftCourse.course_title;
    })
  }

}
