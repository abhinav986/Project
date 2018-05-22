import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Http, URLSearchParams, RequestOptions, Headers } from '@angular/http';

@Injectable()
export class CourseFilterService {

  private searchUrl = '/api/courses/search/filters';
  constructor(private http: Http) { }

  getCourseFilterData(courseName, languages: any, sort: string): Observable<string[]> {

    const myHeaders = new Headers();
    const urlParams = new URLSearchParams();
    urlParams.append('title', courseName);

    if (languages.length > 0) {
      urlParams.append('languages', languages);
    }

    if (sort !== 'default') {
      urlParams.append('sort', 'price');
      urlParams.append('order', sort);
    }

    const options = new RequestOptions({ headers: myHeaders, params: urlParams });
    return this.http.get(this.searchUrl, options)
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
