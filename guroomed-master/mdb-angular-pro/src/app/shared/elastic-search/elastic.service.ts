import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class ElasticService {

  private headers = new Headers({ 'Content-Type': 'application/x-www-form-urlencoded' });
  baseUrl = '/api/courses/search/filters';

  constructor(private http: Http) { }

  searchCourseData(searchString) {
    const body = `query=${searchString}`;
    return this.http.post(this.baseUrl, body, { headers: this.headers })
      .map(searchDdata => searchDdata)
      .catch(this.handleError);
  }

  autoSuggestUrlData(queryStr: string) {
    return this.http.get(`/api/courses/search?query=${queryStr}`)
      .map(autoSuggest => autoSuggest)
      .catch(this.handleError);
  }

  private handleError(error: any) {
    const errMsg = (error.message) ? error.message :
      error.status ? `${error.status} - ${error.statusText}` : 'Server error';
    console.error(errMsg);
    return Observable.throw(errMsg);
  }

}
