import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class MycoursesService {
  myCourseUrl = '/api/courses/mycourses/';
  videoUrl = '/api/courses/curriculum/';
  constructor(private http: HttpClient) { }

  getMyCourses(user_id) {
    return this.http.get(this.myCourseUrl+user_id);
  }

  getMyCourseVideos(course_id) {
    return this.http.get(this.videoUrl+course_id);
  }
}