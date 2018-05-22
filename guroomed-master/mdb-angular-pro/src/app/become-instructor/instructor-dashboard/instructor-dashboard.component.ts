import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';
import { InstructorServiceService } from '../instructor-service/instructor-service.service';

@Component({
  selector: 'app-instructor-dashboard',
  templateUrl: './instructor-dashboard.component.html',
  styleUrls: ['./instructor-dashboard.component.scss']
})
export class InstructorDashboardComponent implements OnInit {

  draftDatalength: number;
  draftData: Array<any>;
  constructor(private nav: NavbarService, private instructorService: InstructorServiceService) { }

  ngOnInit() {
    this.nav.show();
    this.instructorData();
  }

  // Get Instructor Dashboard Data
  instructorData() {
    this.instructorService.getDashboardData(2).subscribe((data) => {
      this.draftDatalength = data['drafts'].length;
      this.draftData = data['drafts'];
    });
  }

}
