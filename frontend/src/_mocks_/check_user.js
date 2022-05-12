import { faker } from "@faker-js/faker";
import { sample } from "lodash";
import axios from "axios";

// ----------------------------------------------------------------------

const checkAuthenticated = () => async () => {
  let formNames = [];
  const res = axios
    .get(`${process.env.REACT_APP_API_URL}/forms/get/`)
    .then((res) => {
      for (var i = 0; i < res.data.length; i += 1) {
        formNames.push(res.data[i].name);
      }
      console.log(formNames);
    });
  return formNames;
};

let x = checkAuthenticated();
console.log("done")
const users = [...Array(24)].map((_, index) => ({
  id: faker.datatype.uuid(),
  name: faker.name.findName(),
}));

export default users;
