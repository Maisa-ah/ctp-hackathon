import axios from "axios";

const API_URL =
  process.env.REACT_APP_URL || "https://crested-talon-233500.uc.r.appspot.com/";

class Api {
  static async request(endpoint, paramsOrData = {}, verb = "get") {
    const token = localStorage.getItem("_token");
    if (token) paramsOrData._token = token;

    try {
      return (
        await axios({
          method: verb,
          url: `${API_URL}/${endpoint}`,
          [verb === "get" ? "params" : "data"]: paramsOrData,
        })
      ).data;
    } catch (err) {
      let message = err.response.data.message;
      throw Array.isArray(message) ? message : [message];
    }
  }

  static async login(data) {
    let res = await this.request(`account/login/`, data, "post");
    return res;
  }

  static async logout() {
    let res = await this.request(`account/logout/`);
    return res;
  }

  static async register(data) {
    let res = await this.request(`account/registration/`, data, "post");
    return res;
  }

  static async getUsers() {
    let res = await this.request(`account/users/`);
    return res;
  }

  static async getUsers(id) {
    let res = await this.request(`account/${id}/`);
    return res;
  }

  static async getServices() {
    let res = await this.request(`api/service/`);
    return res;
  }

  static async getService(service_code) {
    let res = await this.request(`api/services/${service_code}/`);
    return res;
  }

  static async getSchools() {
    let res = await this.request(`api/schools/`);
    return res;
  }

  static async getSchool(school_code) {
    let res = await this.request(`api/schools/${school_code}/`);
    return res;
  }

  static async getMajors() {
    let res = await this.request(`api/majors/`);
    return res;
  }

  static async getMajor(major_code) {
    let res = await this.request(`api/majors/${major_code}/`);
    return res;
  }

  static async getClass() {
    let res = await this.request(`api/classes/`);
    return res;
  }

  static async getClasses(class_code) {
    let res = await this.request(`api/classes/${class_code}/`);
    return res;
  }

  static async match(data) {
    let res = await this.request(`match/`, { data }, "post");
    return res.user;
  }
}

export default Api;
