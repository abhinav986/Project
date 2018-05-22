import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class CourseDetailService {
  baseUrl = '/api/courses/frontend/show/';
  constructor(private http: HttpClient) { }

  get(course_id): Observable<string[]> {
    return this.http.get(this.baseUrl + course_id)
      .map(data => data)
      .catch(this.handleError);
  }

  private handleError(error: any) {
    const errMsg = (error.message) ? error.message :
      error.status ? `${error.status} - ${error.statusText}` : 'Server error';
    console.error(errMsg);
    return Observable.throw(errMsg);
  }

}
