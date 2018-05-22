import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { MycoursesService } from '../../mycourses/mycourses.service';
import { AuthenticationService } from '../../services/authentication.service';

@Component({
  selector: 'app-coursecontainer',
  templateUrl: './coursecontainer.component.html',
  styleUrls: ['./coursecontainer.component.scss']
})
export class CoursecontainerComponent implements OnInit {
  myCourseData: any;
  public _course: any;

  @Input()
  set courses(courses: any) {
    this._course = courses;
  }

  get courses(): any {
    return this._course;
  }
  constructor(private route: Router, private myCourse: MycoursesService, private authenticationService: AuthenticationService, ) { }

  ngOnInit() {
  }

  courseDetials(id) {
     if (this.authenticationService.loggedIn()) {
      this.myCourse.getMyCourses(localStorage.getItem('user_id'))
        .subscribe(data => {
          this.myCourseData = data['courses'];
          if (this.myCourseData.length != 0) {
            this.myCourseData.find(element => {
              if (element.id == id) {
                this.route.navigate(['mycourses']);
                return true;
              } else {
                this.route.navigate(['coursedetails', id]);
              }
            });
          } else {
            this.route.navigate(['coursedetails', id]);
          }
        });
    } else {
      this.route.navigate(['coursedetails', id]);
    }
  }

}
