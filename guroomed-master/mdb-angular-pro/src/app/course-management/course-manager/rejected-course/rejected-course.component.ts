import { Component, OnInit } from '@angular/core';
import { ManagementService } from '../management.service';

@Component({
  selector: 'app-rejected-course',
  templateUrl: './rejected-course.component.html',
  styleUrls: ['./rejected-course.component.scss']
})
export class RejectedCourseComponent implements OnInit {

  course_status: any;
  comments: any;
  reviewer_name: any;
  reviews: any;
  rejected: any;
  constructor(private managementService: ManagementService) { }

  ngOnInit() {
    this.getRejectedList();
  }

  
  getRejectedList() {
    this.managementService.getRejectedCourse().subscribe(rejected => {
      if (rejected['status'] == 1) {
        this.rejected = rejected['drafts'];
      }
    });
  }

  courseStatus(course_id){
    this.managementService.getCourseStatus(course_id).subscribe( res => {
      this.reviews = res['reviews'];
      this.reviewer_name = res['reviews'][0].user_id;
      this.comments = res['reviews'][0].comments;
      this.course_status = res['reviews'][0].status;
    });
  }

}
