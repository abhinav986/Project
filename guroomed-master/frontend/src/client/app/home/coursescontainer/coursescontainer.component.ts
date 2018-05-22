import { Component, OnInit, SimpleChanges, Input } from '@angular/core';
import {Course} from '../course/course';
import {CourseComponent} from '../course/course.component';

@Component({
  selector: 'app-coursescontainer',
  templateUrl: '../app/home/coursescontainer/coursescontainer.component.html',
  styleUrls: ['../app/home/coursescontainer/coursescontainer.component.css']
})
export class CoursescontainerComponent implements OnInit {
  _courses:any;

  @Input()
  set courses(courses:any) {
    this._courses = (courses) || [];
  }
  get courses(): any { return this._courses; }

   ngOnChanges(changes: SimpleChanges){
   }

  constructor() { }

  ngOnInit() { }

}
