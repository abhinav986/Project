import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CourseManagementRouting } from './course-management.routing';
import { MDBBootstrapModule } from '../typescripts/free';
import { MDBBootstrapModulePro } from '../typescripts/pro';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ManagementNavbarComponent } from './management-navbar/management-navbar.component';
import { FormsModule } from '@angular/forms';
import { ManagementService } from './course-manager/management.service';
import { NewCourseListComponent } from './course-manager/new-course-list/new-course-list.component';
import { ReviewedCourseComponent } from './course-manager/reviewed-course/reviewed-course.component';
import { ManagementDashboardComponent } from './management-dashboard/management-dashboard.component';
import { RejectedCourseComponent } from './course-manager/rejected-course/rejected-course.component';
import { ApprovedCourseComponent } from './course-manager/approved-course/approved-course.component';
import { ReviewerTaskComponent } from './course-manager/reviewer-task/reviewer-task.component';
import { CreateReviewerComponent } from './course-manager/create-reviewer/create-reviewer.component';
import { CourseReviewerComponent } from './course-reviewer/course-reviewer.component';
import { ReviewerService } from './course-reviewer/reviewer.service';
import { ManagerGuard } from '../admin/manager.guard';
import { ReviewerGuard } from '../admin/reviewer.guard';
import { ReviewerListComponent } from './course-manager/reviewer-list/reviewer-list.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    CourseManagementRouting,
    MDBBootstrapModule.forRoot(),
    MDBBootstrapModulePro.forRoot(),
    NgbModule.forRoot(),
  ],
  declarations: [
    ManagementDashboardComponent,
    ManagementNavbarComponent,
    NewCourseListComponent,
    ReviewedCourseComponent,
    CreateReviewerComponent,
    RejectedCourseComponent,
    ApprovedCourseComponent,
    ReviewerTaskComponent,
    CourseReviewerComponent,
    ReviewerListComponent
  ],
  schemas: [NO_ERRORS_SCHEMA],
  providers: [
    ManagementService,
    ReviewerService,
    ManagerGuard,
    ReviewerGuard
  ]
})
export class CourseManagementModule { }
