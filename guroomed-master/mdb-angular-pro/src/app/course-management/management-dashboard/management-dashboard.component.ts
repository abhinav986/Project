import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';

@Component({
  selector: 'app-management-dashboard',
  templateUrl: './management-dashboard.component.html',
  styleUrls: ['./management-dashboard.component.scss']
})
export class ManagementDashboardComponent implements OnInit {

  constructor(private nav: NavbarService) { }

  ngOnInit() {
    this.nav.hide();
  }

}