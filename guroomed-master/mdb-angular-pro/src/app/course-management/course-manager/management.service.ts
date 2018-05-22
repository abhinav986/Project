import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class ManagementService {


  newCourse = 'api/user/dashboard/7/2'; // For new courses
  approvedUrl = 'api/user/dashboard/7/1';
  rejectUrl = 'api/user/dashboard/7/0';
  managerStatus = 'api/user/dashboard/7/';
  overviewUrl = 'api/draft/manager/action/';
  rejectReasonUrl = 'api/draft/reviewer/action/';
  getReviewerList = '/api/draft/assign/0';
  createReviewerUrl = 'api/user/reviewer/create/';
  sendToReviewerUrl = 'api/draft/assign/';
  categoryListUrl = 'api/user/reviewer/create';
  reviewerListURL = 'api/user/reviewer/listing/';

  courseStatus = 'api/draft/';

  private headers = new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' });
  constructor(private http: HttpClient) { }

  getCourseStatus(course_id) {
    return this.http.get(this.courseStatus + course_id);
  }

  getReviewerListData() {
    return this.http.get(this.getReviewerList);
  }

  getReasonList() {
    return this.http.get(this.rejectReasonUrl);
  }

  getDraftCourses() {
    return this.http.get(this.newCourse);
  }

  // Function to approved coures based on review
  getApprovedCourse() {
    return this.http.get(this.approvedUrl);
  }

  // Function to reject coures based on review
  getRejectedCourse() {
    return this.http.get(this.rejectUrl);
  }

  // Function to assign reviewer to particular courses
  assignedReviewer(course_id, reviewerData) {
    let formData = new FormData();
    formData.append('group_id', '8');
    reviewerData.reviewer_name.forEach((id) => {
      formData.append('user_ids[]', id);
    });
    return this.http.post(this.sendToReviewerUrl + course_id + '/', formData);
  }

  courseOverview(course_id, comment, status) {
    let body;
    if (status == 1) {
      body = `course_id=${course_id}&comments=${comment}&status=${status}`;
    } else {
      body = `course_id=${course_id}&comments=${comment.reject_comment}&status=${status}&reason_rejected=${comment.reject_reason}`;
    }
    return this.http.post(this.overviewUrl, body, { headers: this.headers });
  }

  // Function to get data based on course category
  getCourseCategory() {
    return this.http.get(this.categoryListUrl);
  }

  // Function to create new reviewer
  createNewReviewer(reviewer) {
    let body = `sub_cat_id=${reviewer.category}&first_name=${reviewer.first_name}&last_name=${reviewer.last_name}&email=${reviewer.email}&password1=${reviewer.password}&password2=${reviewer.confirm_password}`;
    return this.http.post(this.createReviewerUrl, body, { headers: this.headers });
  }

  // Function to get reviewer list
  getReviewerRecord() {
    return this.http.get(this.reviewerListURL + localStorage.getItem('user_id') + '/0/');
  }

}