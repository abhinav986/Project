import { Component, OnInit,Input,SimpleChanges  } from '@angular/core';

@Component({
  selector: 'app-beinstructor',
  templateUrl: '../app/home/beinstructor/beinstructor.component.html',
  styleUrls: ['../app/home/beinstructor/beinstructor.component.css']
})
export class BeinstructorComponent implements OnInit {
	_data:any;
  @Input()
  set data(data:any) {
    this._data = (data) || {name:"peace"};
  }
  get data(): any { return this._data; }

  constructor() { }

  ngOnInit() {
  }

}
