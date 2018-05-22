import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../../shared/navbarService/navbar.service';
import { ActivatedRoute, Router } from '@angular/router';
import { InstructorServiceService } from '../instructor-service/instructor-service.service';
import { ToastService } from '../../typescripts/pro';

@Component({
  selector: 'app-course-manage',
  templateUrl: './course-manage.component.html',
  styleUrls: ['./course-manage.component.scss']
})
export class CourseManageComponent implements OnInit {

  loading: boolean;
  course_id: any;
  constructor(private toastrService: ToastService, private nav: NavbarService, private route: ActivatedRoute, private router: Router, private instructorService: InstructorServiceService) { }

  ngOnInit() {
    this.nav.show();
  }

  submitForReview() {
    this.loading = true;
    this.course_id = this.route.snapshot.params.id;
    this.instructorService.forReview(this.course_id).subscribe(data => {
      if (data['status'] == 1) {
        this.loading = false;
        let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
        this.toastrService.success('', 'Your Course is successfully submitted for review', options);
        this.router.navigate(['instructor/dashboard']);
      }
    });
  }

}
