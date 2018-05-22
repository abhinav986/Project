import { Component, OnInit } from '@angular/core';
import { ReviewerService } from './reviewer.service';
import { ToastService } from '../../typescripts/pro';
import { ManagementService } from '../course-manager/management.service';

@Component({
  selector: 'app-course-reviewer',
  templateUrl: './course-reviewer.component.html',
  styleUrls: ['./course-reviewer.component.scss']
})
export class CourseReviewerComponent implements OnInit {

  reasonSelect: any;
  options: { closeButton: boolean; tapToDismiss: boolean; positionClass: string; };
  draftsCourse: any;
  rejectReason = {};
  approvedReason = {};
  constructor(private reviewerService: ReviewerService, private toastService: ToastService, private managementService: ManagementService) { }

  ngOnInit() {
    this.getDashboardData();
    this.options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };

    this.managementService.getReasonList().subscribe(reasonList => {
      this.reasonSelect = reasonList['reasons_rejected'];
    });
  }

  getDashboardData() {
    this.reviewerService.dashboardData(2).subscribe(data => {
      this.draftsCourse = data['drafts'];
    });
  }

  approvedCourse(course_id) {
    var approved_comment = this.approvedReason['approved_comment'];
    this.reviewerService.courseOverview(course_id, approved_comment, 1).subscribe(resData => {
      if (resData['status'] == 1) {
        this.toastService.success('', resData['msg'], this.options);
      }
    });
  }

  rejectCourse(course_id) {
    this.reviewerService.courseOverview(course_id, this.rejectReason, 0).subscribe(data => {
      if (data['status'] == 1) {
        // this.router.navigate(['/course-status']);
        this.toastService.success('', data['msg'], this.options);
      }
    });
  }

}
