import { Component, OnInit } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';

@Component({
  selector: 'app-mycourses',
  templateUrl: './mycourses.component.html',
  styleUrls: ['./mycourses.component.scss']
})
export class MycoursesComponent implements OnInit {

  constructor( private nav: NavbarService) { }

  ngOnInit() {
    this.nav.show();
  }

}
