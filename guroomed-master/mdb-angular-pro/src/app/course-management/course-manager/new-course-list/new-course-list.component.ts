import { Component, OnInit, OnDestroy } from '@angular/core';
import { ManagementService } from '../management.service';
import { Subscription } from 'rxjs/Subscription';
import { Observable } from 'rxjs/Observable';
import { ToastService } from '../../../typescripts/pro';

@Component({
  selector: 'app-course-list',
  templateUrl: './new-course-list.component.html',
  styleUrls: ['./new-course-list.component.scss']
})
export class NewCourseListComponent implements OnInit, OnDestroy {

  reasonSelect: any;
  comments: any;
  course_status: any;
  reviewer_name: string;
  reviews: any;
  options: { closeButton: boolean; tapToDismiss: boolean; positionClass: string; };
  draftsCourse: any;
  optionsSelect: Array<any>;
  rejectReason = {};
  approvedReason = {};
  reviewerName = {};

  private autoRefresh: Subscription;
  private courseSubscription: Subscription;

  constructor(private managementService: ManagementService, private toastService: ToastService) { }

  ngOnInit() {
    this.options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
    this.getNewCourses();
  }

  getNewCourses() {
    this.managementService.getReviewerListData().subscribe(reviewerList => {
      this.optionsSelect = reviewerList['reviewers'];
    });

    this.managementService.getReasonList().subscribe(reasonList => {
      this.reasonSelect = reasonList['reasons_rejected'];
    });
    this.refreshData();
  }

  assignReviewer(course_id) {
    this.managementService.assignedReviewer(course_id, this.reviewerName).subscribe(res => {
      if (res['status'] == 1) {
        this.toastService.success('', 'Successfully asigned...! ', this.options);
      } else {
        this.toastService.error('', 'Something went wrong ', this.options);
      }
    });
  }

  courseStatus(course_id) {
    this.managementService.getCourseStatus(course_id).subscribe(res => {
      if (res['reviews'].length > 0) {
        this.reviews = res['reviews'];
      }
    });
  }

  approvedCourse(course_id) {
    var approved_comment = this.approvedReason['approved_comment'];
    this.managementService.courseOverview(course_id, approved_comment, 1).subscribe(data => {
      if (data['status'] == 1) {
        this.toastService.success('', data['msg'], this.options);
      }
    });
  }

  rejectCourse(course_id) {
    this.managementService.courseOverview(course_id, this.rejectReason, 0).subscribe(data => {
      if (data['status'] == 1) {
        // this.router.navigate(['/course-status']);
        this.toastService.success('', data['msg'], this.options);
      }
    })
  }

  private refreshData(): void {
    this.courseSubscription = this.managementService.getDraftCourses().subscribe(data => {
      if (data['status'] == 1) {
        this.draftsCourse = data['drafts'];
        this.autoRefreshData();
      }
    });
  }

  private autoRefreshData(): void {
    this.autoRefresh = Observable.timer(100000).subscribe(() => this.refreshData());
  }

  ngOnDestroy() {
    if (this.autoRefresh) {
      this.autoRefresh.unsubscribe();
    }

    if (this.courseSubscription) {
      this.courseSubscription.unsubscribe();
    }
  }

}