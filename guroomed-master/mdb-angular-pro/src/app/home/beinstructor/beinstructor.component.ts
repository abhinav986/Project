import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-beinstructor',
  templateUrl: './beinstructor.component.html',
  styleUrls: ['./beinstructor.component.scss']
})
export class BeinstructorComponent implements OnInit {
  _data: any;
  @Input()
  set data(data: any) {
    this._data = (data) || { name: "peace" };
  }
  get data(): any { return this._data; }


  constructor() { }

  ngOnInit() {
  }

}
