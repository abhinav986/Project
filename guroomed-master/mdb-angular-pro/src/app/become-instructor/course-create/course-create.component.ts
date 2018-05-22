import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';
import { Router } from '@angular/router';
import { InstructorServiceService } from '../instructor-service/instructor-service.service';
import { ToastService } from '../../typescripts/pro';

@Component({
  selector: 'app-course-create',
  templateUrl: './course-create.component.html',
  styleUrls: ['./course-create.component.scss']
})
export class CourseCreateComponent implements OnInit {
  courseCreate: any = {}
  constructor(private nav: NavbarService, private router: Router, private instructorService: InstructorServiceService, private toastrService: ToastService, ) { }

  ngOnInit() {
    this.nav.show();
  }

  onCreateCourseTitle() {
    this.instructorService.createCourse(this.courseCreate).subscribe(res => {
      if (res['status'] == 1) {
        this.router.navigate(['instructor', 'course', 'manage', res['course_id'], 'basics']);
      } else if (res['status'] == 0) {
        let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
        this.toastrService.info('', res['error'], options);
      }
    });
  }
}