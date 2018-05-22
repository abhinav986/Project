import { Component, OnInit } from '@angular/core';

@Component({
  templateUrl: './admin.component.html'
})
export class AdminComponent implements OnInit {
  currentUser: string;
  constructor() { }

  ngOnInit() {
    this.currentUser = localStorage.getItem('currentUser')
  }
}
