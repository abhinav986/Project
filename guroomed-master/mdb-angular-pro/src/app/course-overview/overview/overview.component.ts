import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ManagementService } from '../../course-management/course-manager/management.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss']
})
export class OverviewComponent implements OnInit {

  overViewCourse: any;
  course_id: any;
  constructor(private managementService: ManagementService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.course_id = this.route.snapshot.parent.params.id;
    this.overView(this.course_id)
  }

  overView(course_id) {
    this.managementService.getCourseStatus(course_id).subscribe(res => {
      if (res['status'] == 1) {
        this.overViewCourse = res['draft_course'];
      }
    });
  }
}
