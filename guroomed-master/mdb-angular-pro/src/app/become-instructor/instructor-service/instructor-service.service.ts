import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class InstructorServiceService {

  dashboardUrl = 'api/user/dashboard/1/'; // 1 is group Id
  emailVerifyUrl = 'api/courses/instructor/activate/';
  createCourseUrl = 'api/draft/create/';
  courseBasicsUrl = 'api/draft/course-basics/';
  courseGoalsUrl = 'api/draft/course-goals/';
  reviewUrl = '/api/draft/submit/';
  getListUrl = 'api/draft/create?id=';
  curriculumSectionUrl = 'api/draft/curriculum-section/';
  getCurriculumDataUrl = 'api/draft/curriculum/';
  curriculumLectureUrl = 'api/draft/curriculum-lecture/';
  storeQuizUrl = 'api/quiz/store'; // store quiz based in section id
  addQuizquestionUrl = 'api/quiz/question/store'; // store quiz question based on quiz id
  private headers = new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' });
  constructor(private http: HttpClient) { }

  // Get List of data
  getList(course_id) {
    return this.http.get(this.getListUrl + course_id);
  }

  // Get Item to display on instructor dashboard
  getDashboardData(status) {
    return this.http.get(this.dashboardUrl + status + '/');
  }

  // To create course title
  createCourse(courseCreate) {
    let body = `course_title=${courseCreate.course_title}`;
    return this.http.post(this.createCourseUrl, body, { headers: this.headers });
  }

  // Email verification for new instructor
  emailVerification(uidb64, token) {
    return this.http.get(this.emailVerifyUrl + uidb64 + '/' + token);
  }

  // Save course basics details like: title, subtitle etc.
  saveCourseBasics(course_id, basicCourse, fileToUpload, videoFileToUpload) {
    var formData: FormData = new FormData();
    formData.append('course_title', basicCourse.course_title);
    formData.append('course_subtitle', basicCourse.course_subtitle);
    formData.append('language', basicCourse.language);
    formData.append('level', basicCourse.level);
    formData.append('category', basicCourse.category);
    formData.append('photo_link', fileToUpload, fileToUpload.name);
    formData.append('course_price', basicCourse.course_price);

    if (videoFileToUpload != undefined) {
      formData.append('preview_video', videoFileToUpload, videoFileToUpload.name);
    }
    return this.http.post(this.courseBasicsUrl + course_id + '/', formData);
  }

  // Save course goals like: requirement, description etc
  saveCourseGoals(course_id, test1, test2, test3) {
    let body = `knowledgeRequired=${test1}&targetStudent=${test2}&learnGoal=${test3}`;
    return this.http.post(this.courseGoalsUrl + course_id + '/', body, { headers: this.headers });
  }

  // Final submit to review
  forReview(course_id) {
    return this.http.post(this.reviewUrl + course_id + '/', { headers: this.headers });
  }

  // Add Curriculum section 
  addCurriculum(course_id, sectionName, orderNo) {
    let body = `title=${sectionName.section_name}&order_num=${orderNo}&no_lectures=${0}&duration=${0}`;
    return this.http.post(this.curriculumSectionUrl + course_id + '/', body, { headers: this.headers });
  }

  // Get curriculum data
  getCurriculum(course_id) {
    return this.http.get(this.getCurriculumDataUrl + course_id);
  }

  // Add Quiz title and description
  addCurriculumQuiz(section_id, addQuiz) {
    let body = `course_section_id=${section_id}&title=${addQuiz.quiz_title}&description=${addQuiz.quiz_description}`;
    return this.http.post(this.storeQuizUrl, body, { headers: this.headers })
  }

  // Add Quiz questions and answers
  addQuizQuestion(quizId, order_no, content, status, type_id, answer) {
    let body = `quiz_id=${quizId}&content=${content.question}&order=${order_no}&status=${status}&type_id=${type_id}&answer=${answer}`;
    return this.http.post(this.addQuizquestionUrl, body, { headers: this.headers })
  }

  // Save lectures details like title, description, order_num, video, lecture type
  addCurriculumLectures(section_id, addLecture, orderNo, videoFileToUpload) {
    var formData = new FormData();
    formData.append('title', addLecture.lecture_name);
    formData.append('description', addLecture.description);
    formData.append('order_num', orderNo);
    formData.append('lecture_type', 'none');
    formData.append('video', videoFileToUpload, videoFileToUpload.name);
    return this.http.post(this.curriculumLectureUrl + section_id + '/', formData);
  }

  // Get New Token based on instructor signup using email varification link
  getToken() {
    return this.http.get('api/user/auth/');
  }
}
