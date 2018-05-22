import { Component, OnInit, Input, SimpleChanges } from '@angular/core';
import {Course} from './course';

@Component({
  selector: 'app-course',
  templateUrl: '../app/home/course/course.component.html',
  styleUrls: ['../app/home/course/course.component.css']
})
export class CourseComponent implements OnInit {
    _data:any;
    @Input()
  set data(data:any) {
    this._data = (data) || {name:"peace"};
  }
  get data(): any { return this._data; }
  constructor() {}


  ngOnInit() {}

}
