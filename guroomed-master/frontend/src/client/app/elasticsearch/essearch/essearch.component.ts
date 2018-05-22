import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-essearch',
  templateUrl: '../../../app/elasticsearch/essearch/essearch.component.html',
  styleUrls: ['../../../app/elasticsearch/essearch/essearch.component.css']
})
export class EssearchComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  searchCourses(){
  	alert("Started courses search");
  }

}
