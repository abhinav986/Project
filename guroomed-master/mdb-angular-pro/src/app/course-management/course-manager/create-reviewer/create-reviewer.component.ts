import { Component, OnInit } from '@angular/core';
import { ToastService } from '../../../typescripts/pro';
import { ManagementService } from '../management.service';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-reviewer',
  templateUrl: './create-reviewer.component.html',
  styleUrls: ['./create-reviewer.component.scss']
})
export class CreateReviewerComponent implements OnInit {

  loading: boolean;
  categoryList: any;
  newReviewer = {};
  constructor(private toastService: ToastService, private managementService: ManagementService, private location: Location, private router: Router) { }

  ngOnInit() {
    this.getCategory();
  }

  getCategory() {
    this.managementService.getCourseCategory().subscribe(list => {
      this.categoryList = list['sub_cats'];
    })
  }

  createReviewer() {
    let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
    if ((this.newReviewer['category'] == undefined) || (this.newReviewer['first_name'] == undefined) || (this.newReviewer['last_name'] == undefined) || (this.newReviewer['email'] == undefined) || (this.newReviewer['password'] == undefined) || (this.newReviewer['confirm_password'] == undefined)) {
      return this.toastService.error('', 'Please fill all the mandatory field', options);
    }

    if (this.newReviewer['password'] != this.newReviewer['confirm_password']) {
      this.toastService.error('', 'Password not matched', options);
      return false;
    }
    this.loading = true;
    this.managementService.createNewReviewer(this.newReviewer).subscribe(data => {
      this.loading = false;
      if (data['status'] == 1) {
        this.toastService.success('', data['msg'], options);
        this.router.navigate(['/course-management', 'reviewer-list']);
      } else {
        this.toastService.error('', data['error'], options);
      }
    });
  }

  cancel() {
    this.location.back(); // <-- go back to previous location on cancel
  }

}
