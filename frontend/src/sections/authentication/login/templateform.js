import * as Yup from "yup";
import { useState } from "react";
import { Link as RouterLink, useNavigate, Navigate } from "react-router-dom";
import { useFormik, Form, FormikProvider, connect } from "formik";
import { connect as connectRedux } from "react-redux";
import { login } from "../../../actions/auth";
import Page from "../../../components/Page";
import { styled } from "@mui/material/styles";
import { Container } from "@mui/material";
import axios from "axios";
import { faker } from "@faker-js/faker";
import Scrollbar from "../../../components/Scrollbar";

// material
import {
  Link,
  Stack,
  Checkbox,
  TextField,
  IconButton,
  InputAdornment,
  FormControlLabel,
} from "@mui/material";
import { LoadingButton } from "@mui/lab";

// component
import Iconify from "../../../components/Iconify";

// ----------------------------------------------------------------------
const RootStyle = styled(Page)(({ theme }) => ({
  [theme.breakpoints.up("md")]: {
    display: "flex",
  },
}));

const ContentStyle = styled("div")(({ theme }) => ({
  maxWidth: 580,
  margin: "auto",
  display: "flex",
  minHeight: "100vh",
  flexDirection: "column",
  justifyContent: "center",
  padding: theme.spacing(12, 0),
}));

const divStyle = {
  "margin-top": "24px",
};

function getFormName(url) {
  let name = url.substr(20, url.length);
  let formName = "";
  let index = 0;
  while (index < name.length) {
    if (name[index] == "%") {
      index += 3;
      formName += " ";
      continue;
    }
    formName += name[index];
    index += 1;
  }
  console.log(formName);
  return formName;
}

function FormData({ login, isAuthenticated }) {
  let formName = getFormName(window.location.pathname);
  const config = {
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  };
  const body = JSON.stringify({ name: formName });
  const [loadPage, setLoadPage] = useState(0);
  const [formFields, setFormFields] = useState([]);

  const res = axios
    .post(
      `${process.env.REACT_APP_API_URL}/forms/get_form_fields/`,
      body,
      config
    )
    .then((res) => {
      let formNames = [];
      for (var i = 0; i < res.data.length; i += 1) {
        formNames.push([res.data[i].fieldName, res.data[i].background]);
      }
      const formField = [...Array(formNames.length)].map((_, index) => ({
        id: faker.datatype.uuid(),
        background: formNames[index][1],
        fieldName: formNames[index][0],
      }));
      console.log(formField);
      if (loadPage == 0) {
        setLoadPage(1);
        setFormFields(formField);
      }
    });

  return (
    <RootStyle title="Login | Minimal-UI">
      <Container maxWidth="xl">
        <ContentStyle>
          <Scrollbar>
            <div style={divStyle}></div>
            <Stack spacing={3}>
              {formFields.map((field) => {
                let namex = field.fieldName;
                return (
                  <TextField
                    fullWidth
                    label={namex}
                    key={field.id}
                    // error={Boolean(touched.namex && errors.namex)}
                    // helperText={touched.namex && errors.namex}
                  />
                );
              })}
            </Stack>
          </Scrollbar>
        </ContentStyle>
      </Container>
    </RootStyle>
  );
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connectRedux(mapStateToProps, { login })(FormData);
