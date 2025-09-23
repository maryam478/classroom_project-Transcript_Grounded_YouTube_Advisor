Geocenter, Copenhagen 

13-15 September 2007 

Instructors: Mary C. Hill (US Geological Survey, USA)

                    Matthew Tonkin (SS Papadopulos and Associates, USA)

      

# Calibration, Sensitivity Analysis and Uncertainty of Groundwater Models  

- These slides were developed for classes coordinated by Mary Hill or Claire Tiedeman since 1992. The slides are freely available from the web site for the text book by Hill and Tiedeman (2007, Wiley) at http://water.usgs.gov/lookup/get?research/hill_tiedeman_book. 
- Contributors to the slides include 

Mary C. Hill             Claire R. Tiedeman                                           U.S. 

Richard L. Cooley (retired)                                                      Geological

Edward Banta                                                                                 Survey

Marshall Gannett      D. Matthew Ely

Arlen Harbaugh        Howard Reeves

Steffen Mehl (now at California State Univ, Chico)

Evan Anderman, formerly Calibra Consultants, McDonald Morrissey

Matt Tonkin, SS Papadopulos and Associates 

Gilbert Barth, SS Papadopulos and Associates 

Heidi Christensen Barlebo, GEUS

Frank Smits,  Dutch hydrologist

Willem Jan Zaadnoordijk, Royal Haskoning, the Netherlands

# Instructors

Mary Hill – US Geological Survey, Boulder, CO, USA. 

- Focus: Improve how we simulate ground-water systems and evaluate model uncertainty. Wrote MODFLOWP, PCG2 solver, co-author of, for example, MODFLOW-2000, HUF, UCODE_2005, MMA, OPR-PPR.
- BA, Geology and Business Administration, Hope College, Holland, MI.
- PhD, Water Resources, Civil Engineering, Princeton University

Matt Tonkin – Hydrogeologist, SS Papadopulos &amp; Assoc, Inc.

		          	  PhD student, U. of Queensland, Australia

	  Focus: Computationally efficient predictive analysis through regularized inversion

		    Co-author – MOD-PREDICT, OPR-PPR

		    Host – PEST technical support forum	

	  BA, Applied and Environmental Geology, Birmingham University, UK

	  MS, Hydrogeology, Birmingham University, UK

# You!

Student introductions

Name

Your country and, briefly, major national ground-water problems

Employer/school

Experience in ground-water modeling

			inverse methods

			statistics

Graphical interface experience/preference

What do you want to obtain from this course?

To what modeling project(s) do you plan to apply the methods?

# Primary Documents Used in the Course

Effective Groundwater Model Calibration, with Analysis of Data, Sensitivity, Predictions, and Uncertainty 

(Hill and Tiedeman, 2007, Wiley). 

Program Documentation for MODFLOW-2005, MODPATH, UCODE_2005, OPR-PPR, MMA, PEST

For all programs, documentation PDF files are provided and also can be downloaded from the internet.

Additional MODFLOW documentation can be found on: http://water.usgs.gov/nrp/gwsoftware/modflow2005/modflow2005.html

# Computer Software

- Parameter-estimation with UCODE_2005
- Class provides much of the background needed to use MODFLOW-2000, UCODE_2005, PEST, OSTRICH or any other inverse modeling code
- UCODE-2005: 
- PEST – Parameter ESTimation software

 MODFLOW2005    

-   USGS three-dimensional, transient, ground-water flow computer program. 

-    USGS Universal inverse modeling CODE 

-    Constructed using the JUPITER API

-    Use with any model. 

-    If used with perturbation sensitivities, consequences investigated by Hill and Østerby, 2003; Mehl and Hill, 2002

-    Parameter-estimation method expanded from that in MODFLOW-2000. 

-    Model independent like UCODE_2005

-    Includes additional very useful parameterization and regularization capabilities.

# Perspective 

The methods and guidelines are broadly applicable, but taught using ground-water modeling examples.

There are about as many opinions about how to construct and use models as there are people working with models. There are a number of ongoing methods to standardize ground-water model construction and use. For example, HarmoniQua (€5 million over 5 years), Germany, Australia, New Zeeland, USEPA, USGS, ASTM, …See review by Hill et al. (2004, conf. proceedings, FEM-MODFLOW)

No set of methods and ideas is best in all circumstances, but we are hoping that by learning one set of methods and ideas, you will improve how you develop models, and be in a position to improvise using new ideas as you come across new, useful ideas.

- Methods for sensitivity analysis, data assessment, model calibration, and evaluation of model uncertainty. These methods take advantage of the quantitative connections provided models between:
- Guidelines that describe how to use the methods presented, with emphasis on applications to ground-water models. 

          observations – parameters - predictions

# Purpose of Course

# Major steps of ground-water modeling

Hydrologic and hydrogeologic data

Relate to model inputs

Dependent variable observations

Relate to model outputs -- calibration

Ground-Water Model -- parameters

Predictions 

Prediction uncertainty

Societal decisions

# Major steps of ground-water modeling

Hydrologic and hydrogeologic data

Relate to model inputs

Dependent variable observations

Relate to model outputs -- calibration

Ground-Water Model -- parameters

Predictions 

Prediction uncertainty

Societal decisions

# We consider calibration with analysis of data, sensitivities, predictions, and uncertainty

observations – parameters - predictions

- Estimate parameters with observations using a gradient-based method (versus global optimization). Gradient methods are much faster but can get stuck in local minima.
- Use sensitivity analysis to investigate relations between observations, parameters, and predictions.

# Sensitivity analysis measures taught

Observations – Parameters - Predictions

dss                                  pss

css                                  ppr

pcc

leverage

Parameter cv

AIC

BIC

DFBETAS 

Cook’s D

opr

Observations ---------------- Predictions

# Field and synthetic examples

- Field examples are used to demonstrate how the methods and guidelines are used in practice. 
- We begin the class with a study of the Death Valley regional ground-water system in California and Nevada, USA.
- A synthetic example is used to investigate the methods and guidelines in a situation for which the truth is known.
- A synthetic test case with a model development phase followed by a predictions phase is developed over the length of the course. 

# Common questions that can be addressed by the methods taught here 

- How much and what model complexity can the observations support?
- Are any of the estimated parameter values dominated by a single observation? 
- What model parameters are important to the things I need to predict?
- What data should be collected to improve the predictions? 
- Which conceptual model of the system is likely to produce better predictions?
- How certain are the predictions?