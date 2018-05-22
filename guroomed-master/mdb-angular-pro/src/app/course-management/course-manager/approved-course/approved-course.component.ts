import { Component, OnInit } from '@angular/core';
import { ManagementService } from '../management.service';

@Component({
  selector: 'app-approved-course',
  templateUrl: './approved-course.component.html',
  styleUrls: ['./approved-course.component.scss']
})
export class ApprovedCourseComponent implements OnInit {

  approved: Object;
  constructor(private managementService: ManagementService) { }

  ngOnInit() {
    this.getApprovedList();
  }

  getApprovedList() {
    this.managementService.getApprovedCourse().subscribe(approved => {
      if (approved['status'] == 1) {
        this.approved = approved['drafts'];
      }
    })
  }

}
