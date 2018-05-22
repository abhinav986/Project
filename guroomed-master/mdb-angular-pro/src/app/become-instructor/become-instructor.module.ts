import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { BecomeInstructorRoutingModule } from './become-instructor-routing.module';
import { BecomeInstructorComponent } from './become-instructor.component';
import { MDBBootstrapModulePro } from '../typescripts/pro';
import { MDBBootstrapModule } from '../typescripts/free';
import { InstructorDashboardComponent } from './instructor-dashboard/instructor-dashboard.component';
import { CourseCreateComponent } from './course-create/course-create.component';
import { CourseManageComponent } from './course-manage/course-manage.component';
import { CourseGoalsComponent } from './course-manage/course-goals/course-goals.component';
import { CourseCurriculumComponent } from './course-manage/course-curriculum/course-curriculum.component';
import { CourseBasicsComponent } from './course-manage/course-basics/course-basics.component';
import { CoursePriceCouponsComponent } from './course-manage/course-price-coupons/course-price-coupons.component';
import { CourseCommunicationComponent } from './course-manage/course-communication/course-communication.component';
import { CourseCaptionsComponent } from './course-manage/course-captions/course-captions.component';
import { ImageUploadModule } from "angular2-image-upload";
import { InstructorSignUpComponent } from './instructor-sign-up/instructor-sign-up.component';
import { InstructorLoginComponent } from './instructor-login/instructor-login.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { SignupService } from './instructor-sign-up/signup.service';
import { InstructorServiceService } from './instructor-service/instructor-service.service';
import { InstructorGuard } from '../admin/instructor.guard';
import { QuizComponent } from './course-manage/quiz/quiz.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    BecomeInstructorRoutingModule,
    MDBBootstrapModule.forRoot(),
    MDBBootstrapModulePro.forRoot(),
    ImageUploadModule.forRoot()
  ],
  declarations: [
    BecomeInstructorComponent,
    InstructorDashboardComponent,
    CourseCreateComponent,
    CourseManageComponent,
    CourseGoalsComponent,
    CourseCurriculumComponent,
    CourseBasicsComponent,
    CoursePriceCouponsComponent,
    CourseCommunicationComponent,
    CourseCaptionsComponent,
    InstructorSignUpComponent,
    InstructorLoginComponent,
    ForgotPasswordComponent,
    QuizComponent,
  ],
  providers: [SignupService, InstructorServiceService, InstructorGuard]
})
export class BecomeInstructorModule { }
