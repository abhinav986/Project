import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class ReviewerService {

  reviewerDashboardUrl = 'api/user/dashboard/8/';
  reviewerListUrl = 'api/draft/assign/0';
  overviewUrl = 'api/draft/reviewer/action/';

  private headers = new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' });
  constructor(private http: HttpClient) { }

  dashboardData(status) {
    return this.http.get(this.reviewerDashboardUrl + status);
  }

  reviewerList() {
    return this.http.get(this.reviewerListUrl);
  }

  courseOverview(course_id, overview, status) {
    let body;
    if (status == 1) {
      body = `course_id=${course_id}&comments=${overview}&status=${status}`;
    } else {
      body = `course_id=${course_id}&comments=${overview.reject_comment}&status=${status}&reason_rejected=${overview.reject_reason}`;
    }
    return this.http.post(this.overviewUrl, body, { headers: this.headers });
  }

}
