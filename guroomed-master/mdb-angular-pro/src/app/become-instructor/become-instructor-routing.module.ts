import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BecomeInstructorComponent } from './become-instructor.component';
import { InstructorDashboardComponent } from './instructor-dashboard/instructor-dashboard.component';
import { CourseCreateComponent } from './course-create/course-create.component';
import { CourseManageComponent } from './course-manage/course-manage.component';
import { CourseGoalsComponent } from './course-manage/course-goals/course-goals.component';
import { CourseCurriculumComponent } from './course-manage/course-curriculum/course-curriculum.component';
import { CourseBasicsComponent } from './course-manage/course-basics/course-basics.component';
import { CoursePriceCouponsComponent } from './course-manage/course-price-coupons/course-price-coupons.component';
import { CourseCommunicationComponent } from './course-manage/course-communication/course-communication.component';
import { CourseCaptionsComponent } from './course-manage/course-captions/course-captions.component';
import { InstructorSignUpComponent } from './instructor-sign-up/instructor-sign-up.component';
import { InstructorLoginComponent } from './instructor-login/instructor-login.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { ContentComponent } from '../course-overview/content/content.component';
import { CourseOverviewComponent } from '../course-overview/course-overview.component';
import { OverviewComponent } from '../course-overview/overview/overview.component';
import { QuestionsComponent } from '../course-overview/questions/questions.component';
import { BookmarksComponent } from '../course-overview/bookmarks/bookmarks.component';
import { AnnouncementsComponent } from '../course-overview/announcements/announcements.component';
import { InstructorGuard } from '../admin/instructor.guard';

const routes: Routes = [
  {
    path: 'instructor',
    component: BecomeInstructorComponent
  },
  {
    path: 'instructor/register/instructor-signup',
    component: InstructorSignUpComponent
  },
  {
    path: 'instructor/login/instructor-login',
    component: InstructorLoginComponent
  },
  {
    path: 'instructor/user/forgot-password',
    component: ForgotPasswordComponent,
    canActivate: [InstructorGuard]
  },
  {
    path: 'instructor/dashboard',
    component: InstructorDashboardComponent,
    canActivate: [InstructorGuard]
  },
  {
    path: 'instructor/course/create',
    component: CourseCreateComponent,
    canActivate: [InstructorGuard]
  },
  {
    path: 'instructor/course/draft-content/:id',
    component: CourseOverviewComponent,
    children: [
      { path: 'overview', component: OverviewComponent },
      { path: 'content', component: ContentComponent },
      { path: 'questions', component: QuestionsComponent },
      { path: 'bookmarks', component: BookmarksComponent },
      { path: 'announcements', component: AnnouncementsComponent },
    ]
  },

  {
    path: 'instructor/course/manage/:id',
    component: CourseManageComponent,
    canActivate: [InstructorGuard],
    children: [
      { path: 'basics', component: CourseBasicsComponent },
      { path: 'goals', component: CourseGoalsComponent },
      { path: 'crriculum', component: CourseCurriculumComponent },
      { path: 'price-coupons', component: CoursePriceCouponsComponent },
      { path: 'captions', component: CourseCaptionsComponent },
      { path: 'communication', component: CourseCommunicationComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BecomeInstructorRoutingModule { }
